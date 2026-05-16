lpc17xx_nvic_header = custom_target(
	'nvic.h',
	command: [irq2nvic, '@INPUT@'],
	input: 'irq.json',
	output: 'nvic.h',
	install: false,
)

lpc17xx_vector_nvic = declare_dependency(
	sources: lpc17xx_nvic_header,
)
