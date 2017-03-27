from GD25Q128 import GD25Q128Reader

spi_reader = GD25Q128Reader()
spi_reader.connect("/dev/ttyUSB0")

spi_reader.read_id()

#spi_reader.write_enable()
#spi_reader.parse_SR()
#spi_reader.write_disable()
#spi_reader.parse_SR()

spi_reader.write_rom("flash_compiled.bin")
spi_reader.dump_rom("flash_compiled_verify.bin")

spi_reader.disconnect()