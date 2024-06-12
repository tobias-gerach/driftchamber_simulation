import matplotlib.pyplot as plt
import numpy as np


class OutputModule:
    """
    Module for a nicer visualization of the drift chamber using matplotlib.
    The different field symbols 'o', 'O', and 'X' are converted to integers using Ascii to
    create an imshow plot.
    """
    def __init__(self):
        pass

    def execute(self, datastore):
        chamber = datastore.get('chamber')
        self.Field = datastore.get('HField')

        # Erzeuge hitdata Liste zur Konvertierung in ascii Dezimaldarstellung
        hitdata = []
        for i in self.Field:
            hitdata.append(list(i))
        for i in range(len(hitdata)):
            for j in range(len(hitdata[i])):
                hitdata[i][j] = ord(hitdata[i][j])
                if hitdata[i][j] == 88:
                    hitdata[i][j] += 1000  # Erhoehung der Hit-Integern zur besseren Farbwahl

        fig, ax = plt.subplots(figsize=(20, 10))
        ax.imshow(hitdata, interpolation='nearest')
        ax.axis('off')
        fig.tight_layout(pad=5)
        plt.title('Driftchamber', fontsize='20')


        if datastore.get('BField') == 0:
            Anzahl = datastore.get('particles')
        else:
            Anzahl = 0

        for i in range(Anzahl):
            param = datastore.get('Hough' + str(i))
            a, d = param[0]
            h = chamber.getHight()
            b = chamber.getWidth()
            x = []
            y = []

            # Berechnung der Schnittpunkte der Gerade mit dem Darstellungsbereich (Definitions und Wertebereich)
            if 0 < (d + 1 - (h - 1) * np.sin(a)) / np.cos(a) < b:
                x.append((d + 1 - (h - 1) * np.sin(a)) / np.cos(a))
                y.append(0)
            if 0 < (d + 1) / np.cos(a) < b:
                x.append((d + 1) / np.cos(a))
                y.append(h)
            if 0 < (-d - 1 + (h - 1) * np.sin(a)) / np.sin(a) < h:
                y.append((-d - 1 + (h - 1) * np.sin(a)) / np.sin(a))
                x.append(0)
            if (-d - 1 + (h - 1) * np.sin(a) + (b - 1) * np.cos(a)) / np.sin(a) > 0 and (
                        -d - 1 + (h - 1) * np.sin(a) + (b - 1) * np.cos(a)) / np.sin(a) < h:
                y.append((-d - 1 + (h - 1) * np.sin(a) + (b - 1) * np.cos(a)) / np.sin(a))
                x.append(b)
            ax.plot(x, y, 'g-', linewidth=4.0)

            # Ausgabe der Parameter auf Konsole
            print("Particle", i, ":")
            print("alpha = ", a, "d = ", d)
            print("x = ", x, "y = ", y)

        # Erzeugung der Plots mit Matplotlib

        plt.show()



    def __del__(self):
        print('OutputModule finished')
