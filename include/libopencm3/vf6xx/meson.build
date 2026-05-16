vf6xx_nvic_header = custom_target(
	'nvic.h',
	command: [irq2nvic, '@INPUT@'],
	input: 'irq.json',
	output: 'nvic.h',
	install: false,
)

vf6xx_vector_nvic = declare_dependency(
	sources: vf6xx_nvic_header,
)
