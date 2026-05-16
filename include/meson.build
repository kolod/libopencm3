# This file is part of the libopencm3 project.
#
# Copyright (C) 2023-2025 1BitSquared <info@1bitsquared.com>
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

common_includes = include_directories('.')

target_paths = {
	'stm32f0': 'stm32/f0',
	'stm32f1': 'stm32/f1',
	'stm32f2': 'stm32/f2',
	'stm32f3': 'stm32/f3',
	'stm32f4': 'stm32/f4',
	'stm32f7': 'stm32/f7',
	'stm32g0': 'stm32/g0',
	'stm32g4': 'stm32/g4',
	'stm32h7': 'stm32/h7',
	'stm32l0': 'stm32/l0',
	'stm32l1': 'stm32/l1',
	'stm32l4': 'stm32/l4',
	'stm32u5': 'stm32/u5',
	'gd32f1x0': 'gd32/f1x0',
	'lpc13xx': 'lpc13xx',
	'lpc17xx': 'lpc17xx',
	'lpc43xxm0': 'lpc43xx/m0',
	'lpc43xxm4': 'lpc43xx/m4',
	'nrf51': 'nrf/51',
	'nrf52': 'nrf/52',
	'efm32tg': 'efm32/tg',
	'efm32g': 'efm32/g',
	'efm32lg': 'efm32/lg',
	'efm32gg': 'efm32/gg',
	'efm32hg': 'efm32/hg',
	'efm32wg': 'efm32/wg',
	'ezr32wg': 'efm32/ezr32wg',
	'msp432e4': 'msp432/e4',
	'lm4f': 'lm3s',
}

foreach target_name, target_path : target_paths
	if target_name in target_platforms
		subdir(f'libopencm3/@target_path@')
	endif
endforeach
