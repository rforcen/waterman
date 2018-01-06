import numpy as np

from rendererGL import RendererGL
from strobe144 import strobe144


class WPWidget(RendererGL):
    wp = None
    # color mode=0->strobe144, 1=random
    colors = [np.asarray(strobe144, dtype=np.uint8), np.asarray(255 * np.random.rand(500, 3), dtype=np.uint8)]
    colorMode = 0

    def init(self, gl):
        gl.glCullFace(gl.GL_FRONT)

        gl.glEnable(gl.GL_POINT_SMOOTH)  # round points
        gl.glEnable(gl.GL_LINE_SMOOTH)

        gl.glPointSize(9)
        gl.glLineWidth(2)

        self.randColors()

    def randColors(self):
        np.random.shuffle(self.colors[self.colorMode])
        self.repaint()

    def setColorMode(self, cm):
        self.colorMode = cm
        self.repaint()

    def draw(self, gl):

        def scale(sc):
            gl.glScalef(sc, sc, sc)

        def drawShape():
            def drawPoints():  # points in coords
                gl.glColor3f(1, 0, 0)
                gl.glBegin(gl.GL_POINTS)
                for c in wp.coords: gl.glVertex3fv(c)
                gl.glEnd()

            def drawLines():
                gl.glColor3f(0, 1, 0)
                for face in wp.faces:
                    gl.glBegin(gl.GL_LINE_LOOP)
                    for f in face:
                        gl.glVertex3fv(wp.coords[f])
                    gl.glEnd()

            def drawTrigs():
                for face in wp.faces:
                    gl.glBegin(gl.GL_TRIANGLE_FAN)
                    gl.glColor3ubv(list(self.colors[self.colorMode][len(face)]))
                    for f in face:
                        gl.glVertex3fv(wp.coords[f])
                    gl.glEnd()

            drawTrigs()
            drawLines()
            drawPoints()

        wp = self.wp

        if wp is not None and wp.coords is not None:
            scale(0.42)
            drawShape()

    def setWP(self, wp):
        self.wp = wp
        self.repaint()
