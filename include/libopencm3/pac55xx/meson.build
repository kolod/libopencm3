pac55xx_nvic_header = custom_target(
	'nvic.h',
	command: [irq2nvic, '@INPUT@'],
	input: 'irq.json',
	output: 'nvic.h',
	install: false,
)

pac55xx_vector_nvic = declare_dependency(
	sources: pac55xx_nvic_header,
)
