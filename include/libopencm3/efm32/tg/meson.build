efm32tg_nvic_header = custom_target(
	'nvic.h',
	command: [irq2nvic, '@INPUT@'],
	input: 'irq.json',
	output: 'nvic.h',
	install: false,
)

efm32tg_vector_nvic = declare_dependency(
	sources: efm32tg_nvic_header,
)
