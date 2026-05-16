nrf52_nvic_header = custom_target(
	'nvic.h',
	command: [irq2nvic, '@INPUT@'],
	input: 'irq.json',
	output: 'nvic.h',
	install: false,
)

nrf52_vector_nvic = declare_dependency(
	sources: nrf52_nvic_header,
)
