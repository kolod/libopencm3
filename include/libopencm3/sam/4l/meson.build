sam4l_nvic_header = custom_target(
	'nvic.h',
	command: [irq2nvic, '@INPUT@'],
	input: 'irq.json',
	output: 'nvic.h',
	install: false,
)

sam4l_vector_nvic = declare_dependency(
	sources: sam4l_nvic_header,
)
