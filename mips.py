from pytermgui import tim
import argparse
import subprocess
import tomli

def argparse_init() -> argparse.Namespace:
	parser = argparse.ArgumentParser(description="Mips Selector and Exporter")
	parser.add_argument("-f", "--file",
				help="A toml file for profile creation (default: open CLI selector)",
				required=False)
	args = parser.parse_args()
	return args

# TODO: Add rules to setup and loop
def define_setup(devices: list) -> str:
	insides = ""
	for device in devices:
		io = device.get("io")
		io = io.upper()
		pin_numbers = device.get("pin_numbers")
		for pin in pin_numbers:
			insides = insides + f"\tpinMode({pin}, {io});\n"

	setup = f"void setup(){{\n{insides}\n\tSerial.begin(38400);\n}}"
	return setup

def define_test_loop(devices: list) -> str:
	insides = ""
	for device in devices:
		pin_numbers = device.get("pin_numbers")
		device_type = device.get("device_type")
		if device_type == "rgb_led":
			for pin in pin_numbers:
				insides = insides + f"\tdigitalWrite({pin}, HIGH);\n"
				insides = insides + "\tdelay(500);\n"
				insides = insides + f"\tdigitalWrite({pin}, LOW);\n"
				insides = insides + f"\tdelay(500);\n\n"
		if device_type == "potentiometer":
			insides = insides + f"\tint val = analogRead({pin_numbers[0]});\n"
			insides = insides + f"\tSerial.print(\"Analog {pin_numbers[0]} is: \");\n"
			insides = insides + "\tSerial.println(val);\n"
			insides = insides + "\tdelay(10);\n\n"

	loop = f"void loop(){{\n{insides}}}"
	return loop

def define_loop(devices: list) -> str:
	pass

def make_sketch(name: str, profile: dict):
	tim.print(f"[italic orange]Creating sketch: {name}.ino")
	devices = profile["devices"]
	with open(f"sketches/{name}.ino", "w") as sketch:
		sketch.write(define_setup(devices) + "\n")
		if profile.get("profileInfo").get("test"):
			sketch.write(define_test_loop(devices))
		else:
			sketch.write(define_loop(devices))

	subprocess.run(["arduino-1.8.19/arduino", "--upload", f"sketches/{name}.ino"])

	# TODO: Fix reading serial
	# with open("/dev/ttyACM0", "r") as serial:
	#  	print(serial)

def main():
	args = argparse_init();
	file = vars(args)["file"]
	with open(f"profiles/{file}.toml", "rb") as profile_json:
		profile_dict = tomli.load(profile_json)

	tim.print("[!gradient(51) bold]Welcome to MIPS Selector!")
	if file is None:
		sketch_name = input(tim.parse("[bold orange]Sketch name: "))
	else:
		sketch_name = profile_dict["profile_name"]

	tim.print(f"[bold]{file}")
	make_sketch(sketch_name, profile_dict)

if __name__ == "__main__":
	main()
