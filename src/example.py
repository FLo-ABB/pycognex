from pycognex import NativeInterface


def main():
    try:
        # Create a socket connection to the Cognex In-Sight vision system and log in
        native_interface = NativeInterface('192.168.56.1', 'admin', '')
        execution_and_online = native_interface.execution_and_online
        file_and_job = native_interface.file_and_job
        image = native_interface.image
        settings_and_cells_values = native_interface.settings_and_cells_values

        # Load the job if it is not already loaded
        job_name = "1myJob.job"
        if file_and_job.get_file() != job_name:
            if execution_and_online.get_online() == 1:
                execution_and_online.set_online(0)
            file_and_job.load_file(job_name)

        # Set the system online to be able to trigg the camera and get results
        if execution_and_online.get_online() == 0:
            execution_and_online.set_online(1)

        # Get the last image from the camera
        with open('image.bmp', 'wb') as f:
            f.write(image.read_image()["data"])

        # Get the value of the cell B010 (spreadsheet view)
        print(settings_and_cells_values.get_value_spreadsheet_view("B", 10))
        # Get the value of the symbolic tag "Pattern_1.Fixture.X" (EasyBuilder view)
        print(settings_and_cells_values.get_value_easybuilder_view("Pattern_1.Fixture.X"))
        # Set the value of the symbolic tag "Pattern_1.Horizontal_Offset" to 69.1 (EasyBuilder view)
        settings_and_cells_values.set_float_easybuilder_view("Pattern_1.Horizontal_Offset", 69.1)

        # Close the socket connection
        native_interface.close()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    main()
