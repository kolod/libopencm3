efm32gg_nvic_header = custom_target(
	'nvic.h',
	command: [irq2nvic, '@INPUT@'],
	input: 'irq.json',
	output: 'nvic.h',
	install: false,
)

efm32gg_vector_nvic = declare_dependency(
	sources: efm32gg_nvic_header,
)
