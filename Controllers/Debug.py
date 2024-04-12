class Debug:
    # Atributo estático
    is_debug_mode_on: bool = True

    @staticmethod
    def log(message: any):
        if Debug.is_debug_mode_on:
            print("[LOG]: " + message)