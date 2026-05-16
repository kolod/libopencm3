samd_nvic_header = custom_target(
	'nvic.h',
	command: [irq2nvic, '@INPUT@'],
	input: 'irq.json',
	output: 'nvic.h',
	install: false,
)

samd_vector_nvic = declare_dependency(
	sources: samd_nvic_header,
)
