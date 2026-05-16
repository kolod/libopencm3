gd32f1x0_nvic_header = custom_target(
	'nvic.h',
	command: [irq2nvic, '@INPUT@'],
	input: 'irq.json',
	output: 'nvic.h',
	install: false,
)

gd32f1x0_vector_nvic = declare_dependency(
	sources: gd32f1x0_nvic_header,
)
