efm32g_nvic_header = custom_target(
	'nvic.h',
	command: [irq2nvic, '@INPUT@'],
	input: 'irq.json',
	output: 'nvic.h',
	install: false,
)

efm32g_vector_nvic = declare_dependency(
	sources: efm32g_nvic_header,
)
