foreach(d IN ITEMS pwm/led_fade hello_usb multicore)
  add_subdirectory(${d})
endforeach()
