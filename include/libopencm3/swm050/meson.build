swm050_nvic_header = custom_target(
	'nvic.h',
	command: [irq2nvic, '@INPUT@'],
	input: 'irq.json',
	output: 'nvic.h',
	install: false,
)

swm050_vector_nvic = declare_dependency(
	sources: swm050_nvic_header,
)
