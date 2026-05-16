lpc13xx_nvic_header = custom_target(
	'nvic.h',
	command: [irq2nvic, '@INPUT@'],
	input: 'irq.json',
	output: 'nvic.h',
	install: false,
)

lpc13xx_vector_nvic = declare_dependency(
	sources: lpc13xx_nvic_header,
)
