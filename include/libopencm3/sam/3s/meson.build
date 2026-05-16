sam3s_nvic_header = custom_target(
	'nvic.h',
	command: [irq2nvic, '@INPUT@'],
	input: 'irq.json',
	output: 'nvic.h',
	install: false,
)

sam3s_vector_nvic = declare_dependency(
	sources: sam3s_nvic_header,
)
