lpc43xxm0_nvic_header = custom_target(
	'nvic.h',
	command: [irq2nvic, '@INPUT@'],
	input: 'irq.json',
	output: 'nvic.h',
	install: false,
)

lpc43xxm0_vector_nvic = declare_dependency(
	sources: lpc43xxm0_nvic_header,
)
