msp432e4_nvic_header = custom_target(
	'nvic.h',
	command: [irq2nvic, '@INPUT@'],
	input: 'irq.json',
	output: 'nvic.h',
	install: false,
)

msp432e4_vector_nvic = declare_dependency(
	sources: msp432e4_nvic_header,
)
