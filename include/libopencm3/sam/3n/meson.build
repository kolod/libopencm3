sam3n_nvic_header = custom_target(
	'nvic.h',
	command: [irq2nvic, '@INPUT@'],
	input: 'irq.json',
	output: 'nvic.h',
	install: false,
)

sam3n_vector_nvic = declare_dependency(
	sources: sam3n_nvic_header,
)
