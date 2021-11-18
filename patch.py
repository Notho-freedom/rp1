        self.button = ttk.Button(text="start", command=self.start)
        self.button.pack()
        self.progress = ttk.Progressbar(self.root, orient="horizontal", length=200, mode="determinate")
        self.progress.pack()

        self.bytes = 0
        self.maxbytes = 0

        def start(self):
            self.progress["value"] = 0
            self.maxbytes = 50000
            self.progress["maximum"] = 50000
            self.read_bytes()

        def read_bytes(self):
            '''simulate reading 500 bytes; update progress bar'''
            self.bytes += 500
            self.progress["value"] = self.bytes
            if self.bytes < self.maxbytes:
                # read more bytes after 100 ms
                self.after(100, self.read_bytes)

            self.button = ttk.Button(self.root,text="start", command=start)
            self.button.pack()
            button= Button(self.root,text="start",command=start).pack(pady=10)

        def bar(self):

                self.button = ttk.Button(f_gd,text="start", command=self.start)
                self.button.pack()
                self.progress = ttk.Progressbar(f_gd, orient="horizontal",length=200, mode="determinate")
                self.progress.pack()

                self.bytes = 0
                self.maxbytes = 0

            def start(self):
                self.progress["value"] = 0
                self.maxbytes = 50000
                self.progress["maximum"] = 50000
                self.read_bytes()

            def read_bytes(self):
                '''simulate reading 500 bytes; update progress bar'''
                self.bytes += 500
                self.progress["value"] = self.bytes
                if self.bytes < self.maxbytes:
                    # read more bytes after 100 ms
                    self.after(100, self.read_bytes)
import os
# récupérer le chemin du répertoire courant
path = os.getcwd()
print("Le répertoire courant est : " + path)
# récupérer le nom du répertoire courant
repn = os.path.basename(path)
print("Le nom du répertoire est : " + repn)