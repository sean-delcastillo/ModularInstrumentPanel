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
		pin_number = device.get("pin_number")
		insides = insides + f"\tpinMode({pin_number}, {io});\n"

	setup = f"void setup(){{\n{insides}\n\tSerial.begin(38400);\n}}"
	return setup

def define_test_loop(devices: list) -> str:
	insides = ""
	for device in devices:
		pin_number = device.get("pin_number")
		device_name = device.get("device_name")
		if device_name.__contains__("led"):
			insides = insides + f"\tdigitalWrite({pin_number}, HIGH);\n"
			insides = insides + "\tdelay(500);\n"
			insides = insides + f"\tdigitalWrite({pin_number}, LOW);\n"
			insides = insides + f"\tdelay(500);\n\n"
		if device_name.__contains__("potentiometer"):
			insides = insides + f"\tint val = analogRead({pin_number});\n"
			insides = insides +f"\tSerial.print(\"Analog {pin_number} is: \");\n"
			insides = insides + "\tSerial.println(val);\n"
			insides = insides + "\tdelay(250);\n\n"

	loop = f"void loop(){{\n{insides}}}"
	return loop

def define_loop(devices: list) -> str:
	pass

def make_sketch(name: str, profile: dict):
	tim.print(f"[italic orange]Creating sketch: {name}.ino")
	with open(f"sketches/{name}.ino", "w") as sketch:
		sketch.write(define_setup(profile["devices"]))
		sketch.write("\n")
		if name.__contains__("[TEST]"):
			sketch.write(define_test_loop(profile["devices"]))
		else:
			sketch.write(define_loop(profile["devices"]))

	subprocess.run(["arduino-1.8.19/arduino", "--upload", f"sketches/{name}.ino"])

def main():
	args = argparse_init();
	file = vars(args)["file"]
	with open(f"profiles/{file}.toml", "rb") as profile_json:
		profile_dict = tomli.load(profile_json)
	print(profile_dict)

	tim.print("[!gradient(51) bold]Welcome to MIPS Selector!")
	if file is None:
		sketch_name = input(tim.parse("[bold orange]Sketch name: "))
	else:
		sketch_name = profile_dict["profile_name"]

	make_sketch(sketch_name, profile_dict)

if __name__ == "__main__":
	main()
