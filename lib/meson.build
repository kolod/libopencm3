# This file is part of the libopencm3 project.
#
# Copyright (C) 2023 1BitSquared <info@1bitsquared.com>
# Written by Rachel Mant <git@dragonmux.network>
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# Start by bringing in all the utility components like USB and Ethernet
subdir('ethernet')
subdir('usb')
subdir('cm3')

locm3_ld_script_path = meson.current_source_dir()

# Now take the platform target and map it to a suitable target family
build_stm32 = false
build_lm4f = false
build_gd32 = false
build_lpc13xx = false
build_lpc17xx = false
build_lpc43xx = false
build_nrf = false
build_efm32 = false
build_msp432 = false
build_sam = false
build_vf6xx = false
build_swm050 = false
build_pac55xx = false
build_lm3s = false
foreach target_platform : target_platforms
	if target_platform.startswith('stm32')
		build_stm32 = true
	endif
	if target_platform == 'lm4f'
		build_lm4f = true
	endif
	if target_platform == 'lm3s'
		build_lm3s = true
	endif
	if target_platform == 'gd32f1x0'
		build_gd32 = true
	endif
	if target_platform == 'lpc13xx'
		build_lpc13xx = true
	endif
	if target_platform == 'lpc17xx'
		build_lpc17xx = true
	endif
	if target_platform == 'lpc43xxm4' or target_platform == 'lpc43xxm0'
		build_lpc43xx = true
	endif
	if target_platform == 'nrf51' or target_platform == 'nrf52'
		build_nrf = true
	endif
	if target_platform == 'efm32tg' or target_platform == 'efm32g' or target_platform == 'efm32lg' or target_platform == 'efm32gg' or target_platform == 'efm32hg' or target_platform == 'efm32wg' or target_platform == 'ezr32wg'
		build_efm32 = true
	endif
	if target_platform == 'msp432e4'
		build_msp432 = true
	endif
	if target_platform == 'sam3a' or target_platform == 'sam3n' or target_platform == 'sam3s' or target_platform == 'sam3u' or target_platform == 'sam3x' or target_platform == 'sam4l' or target_platform == 'samd'
		build_sam = true
	endif
	if target_platform == 'vf6xx'
		build_vf6xx = true
	endif
	if target_platform == 'swm050'
		build_swm050 = true
	endif
	if target_platform == 'pac55xx'
		build_pac55xx = true
	endif
endforeach

if build_stm32
	subdir('stm32')
endif
if build_lm4f
	subdir('lm4f')
endif
if build_lm3s
	subdir('lm3s')
endif
if build_gd32
	subdir('gd32')
endif
if build_lpc13xx
	subdir('lpc13xx')
endif
if build_lpc17xx
	subdir('lpc17xx')
endif
if build_lpc43xx
	subdir('lpc43xx')
endif
if build_nrf
	subdir('nrf')
endif
if build_efm32
	subdir('efm32')
endif
if build_msp432
	subdir('msp432')
endif
if build_sam
	subdir('sam')
endif
if build_vf6xx
	subdir('vf6xx')
endif
if build_swm050
	subdir('swm050')
endif
if build_pac55xx
	subdir('pac55xx')
endif
