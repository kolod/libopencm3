ezr32wg_nvic_header = custom_target(
	'nvic.h',
	command: [irq2nvic, '@INPUT@'],
	input: 'irq.json',
	output: 'nvic.h',
	install: false,
)

ezr32wg_vector_nvic = declare_dependency(
	sources: ezr32wg_nvic_header,
)
