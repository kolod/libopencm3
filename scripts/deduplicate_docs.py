#!/usr/bin/env python3
"""
Documentation Deduplication Script for libopencm3

This script finds identical files across different target documentation directories
and replaces them with a single shared copy, updating all references accordingly.

Common duplicated files in Doxygen documentation:
- jquery.js, doxygen.css, doxygen.js, tabs.css, tabs.js
- dynsections.js, menu.js, menudata.js
- Various PNG/SVG icons and images

Usage: python3 deduplicate_docs.py <deploy_directory>
"""

import os
import sys
import hashlib
import shutil
from pathlib import Path
from collections import defaultdict
import re


def calculate_file_hash(file_path):
    """Calculate SHA256 hash of a file."""
    hash_sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_sha256.update(chunk)
        return hash_sha256.hexdigest()
    except (IOError, OSError) as e:
        print(f"Warning: Could not read {file_path}: {e}")
        return None


def find_duplicate_files(deploy_dir):
    """Find all duplicate files by content hash."""
    file_hashes = defaultdict(list)
    
    print("Scanning files for duplicates...")
    
    # Walk through all files in the deploy directory
    for root, dirs, files in os.walk(deploy_dir):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_file_hash(file_path)
            
            if file_hash:
                file_hashes[file_hash].append(file_path)
    
    # Filter to only files that have duplicates
    duplicates = {hash_val: paths for hash_val, paths in file_hashes.items() if len(paths) > 1}
    
    return duplicates


def get_relative_path(from_file, to_file):
    """Calculate relative path from one file to another."""
    from_dir = os.path.dirname(from_file)
    return os.path.relpath(to_file, from_dir)


def update_file_references(file_path, old_ref, new_ref):
    """Update references in HTML, CSS, and JS files."""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Different patterns for different file types
        patterns = [
            # HTML: src="..." and href="..."
            (r'((?:src|href)\s*=\s*["\'])' + re.escape(old_ref) + r'(["\'])', r'\1' + new_ref + r'\2'),
            # CSS: url(...)
            (r'(url\s*\(\s*["\']?)' + re.escape(old_ref) + r'(["\']?\s*\))', r'\1' + new_ref + r'\2'),
            # JS: string references
            (r'(["\'])' + re.escape(old_ref) + r'(["\'])', r'\1' + new_ref + r'\2'),
        ]
        
        original_content = content
        for pattern, replacement in patterns:
            content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
        
        # Only write if content changed
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        
    except (IOError, OSError, UnicodeError) as e:
        print(f"Warning: Could not update {file_path}: {e}")
    
    return False


def deduplicate_files(deploy_dir, duplicates):
    """Deduplicate files and update references."""
    shared_dir = os.path.join(deploy_dir, "shared")
    os.makedirs(shared_dir, exist_ok=True)
    
    deduplication_stats = {
        'files_processed': 0,
        'files_deduplicated': 0,
        'bytes_saved': 0,
        'references_updated': 0
    }
    
    print(f"Created shared directory: {shared_dir}")
    
    for file_hash, duplicate_paths in duplicates.items():
        if len(duplicate_paths) < 2:
            continue
            
        # Skip if files are in different directories but have different names
        filenames = [os.path.basename(path) for path in duplicate_paths]
        if len(set(filenames)) > 1:
            print(f"Skipping files with different names: {filenames}")
            continue
            
        filename = os.path.basename(duplicate_paths[0])
        
        # Skip certain files that might be target-specific
        skip_patterns = ['search', 'navtree', 'index.html', 'files.html', 'globals.html']
        if any(pattern in filename.lower() for pattern in skip_patterns):
            continue
            
        print(f"Deduplicating: {filename} ({len(duplicate_paths)} copies)")
        
        # Choose the canonical file (first one) and move it to shared directory
        canonical_file = duplicate_paths[0]
        shared_file = os.path.join(shared_dir, filename)
        
        # Copy to shared directory
        try:
            shutil.copy2(canonical_file, shared_file)
            file_size = os.path.getsize(canonical_file)
            
            # Update all references to point to the shared file
            all_html_css_js_files = []
            
            # Find all files that might contain references
            for root, dirs, files in os.walk(deploy_dir):
                for file in files:
                    if file.endswith(('.html', '.css', '.js')):
                        all_html_css_js_files.append(os.path.join(root, file))
            
            # Update references in each target directory
            for target_file in duplicate_paths:
                target_dir = os.path.dirname(target_file)
                old_filename = os.path.basename(target_file)
                
                # Calculate relative path from target directory to shared file
                relative_shared_path = get_relative_path(target_file, shared_file)
                
                # Update references in files within this target directory
                for ref_file in all_html_css_js_files:
                    if target_dir in ref_file:  # Only update files in the same target directory
                        if update_file_references(ref_file, old_filename, relative_shared_path):
                            deduplication_stats['references_updated'] += 1
            
            # Remove duplicate files (except the shared one)
            for duplicate_file in duplicate_paths:
                if duplicate_file != canonical_file:
                    try:
                        os.remove(duplicate_file)
                        deduplication_stats['bytes_saved'] += file_size
                        deduplication_stats['files_deduplicated'] += 1
                    except OSError as e:
                        print(f"Warning: Could not remove {duplicate_file}: {e}")
            
            # Remove the original canonical file since we copied it to shared
            try:
                os.remove(canonical_file)
                deduplication_stats['bytes_saved'] += file_size
                deduplication_stats['files_deduplicated'] += 1
            except OSError as e:
                print(f"Warning: Could not remove original {canonical_file}: {e}")
                
            deduplication_stats['files_processed'] += 1
            
        except (IOError, OSError) as e:
            print(f"Error processing {filename}: {e}")
            continue
    
    return deduplication_stats


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 deduplicate_docs.py <deploy_directory>")
        sys.exit(1)
    
    deploy_dir = sys.argv[1]
    
    if not os.path.isdir(deploy_dir):
        print(f"Error: {deploy_dir} is not a valid directory")
        sys.exit(1)
    
    print(f"Starting deduplication of documentation in: {deploy_dir}")
    
    # Find duplicate files
    duplicates = find_duplicate_files(deploy_dir)
    
    if not duplicates:
        print("No duplicate files found.")
        return
    
    print(f"Found {len(duplicates)} sets of duplicate files:")
    total_duplicates = 0
    for file_hash, paths in duplicates.items():
        if len(paths) > 1:
            filename = os.path.basename(paths[0])
            print(f"  {filename}: {len(paths)} copies")
            total_duplicates += len(paths) - 1  # -1 because we keep one copy
    
    print(f"Total duplicate files to remove: {total_duplicates}")
    
    # Perform deduplication
    stats = deduplicate_files(deploy_dir, duplicates)
    
    # Print statistics
    print("\nDeduplication completed!")
    print(f"Files processed: {stats['files_processed']}")
    print(f"Files deduplicated: {stats['files_deduplicated']}")
    print(f"References updated: {stats['references_updated']}")
    print(f"Estimated bytes saved: {stats['bytes_saved']:,} bytes ({stats['bytes_saved']/1024/1024:.2f} MB)")


if __name__ == "__main__":
    main()
