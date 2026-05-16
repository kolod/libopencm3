lpc43xxm4_nvic_header = custom_target(
	'nvic.h',
	command: [irq2nvic, '@INPUT@'],
	input: 'irq.json',
	output: 'nvic.h',
	install: false,
)

lpc43xxm4_vector_nvic = declare_dependency(
	sources: lpc43xxm4_nvic_header,
)
