"""Script to reproduce an avator for situations when a photograph is not
appropriate."""


from math import cos, radians, sin
from PIL import Image, ImageDraw


# If these constants are modified, the drawing *should* adjust automatically.
BACKGROUND_COLOR = (200, 0, 0)
FOREGROUND_COLOR = (255, 255, 255)
STROKE = 10
SIZE = 500
FOREGROUND_RADIUS = 0.48 * SIZE
#FOREGROUND_BBOX = [(10, 10), (490, 490)]
FOREGROUND_BBOX = [(0.02 * SIZE, 0.02 * SIZE), (0.98 * SIZE, 0.98 * SIZE)]

# Create a new image.
avatar = Image.new('RGB', (SIZE, SIZE), BACKGROUND_COLOR)
drawing = ImageDraw.Draw(avatar)


# Draw the 'Y'.
drawing.arc(FOREGROUND_BBOX, 180, 250, FOREGROUND_COLOR, STROKE)
drawing.arc(FOREGROUND_BBOX, 290, 360, FOREGROUND_COLOR, STROKE)
drawing.line(
    [(SIZE / 2, SIZE / 2), (SIZE / 2, FOREGROUND_BBOX[1][1])],
    FOREGROUND_COLOR,
    STROKE
)
drawing.line(
    [(FOREGROUND_BBOX[0][0], SIZE / 2), (FOREGROUND_BBOX[1][0], SIZE / 2)],
    FOREGROUND_COLOR,
    STROKE
)


# Draw the 'M'.
drawing.arc(FOREGROUND_BBOX, 130, 170, FOREGROUND_COLOR, STROKE)
drawing.line(
    [
        (
            SIZE / 2 - FOREGROUND_RADIUS * cos(radians(10)),
            SIZE / 2 + FOREGROUND_RADIUS * sin(radians(10))
        ),
        (
            SIZE / 2 - 3 * STROKE,
            SIZE / 2 + FOREGROUND_RADIUS * sin(radians(10))
        )
    ],
    FOREGROUND_COLOR,
    STROKE
)
drawing.line(
    [
        (
            SIZE / 2 - 3.5 * STROKE,
            SIZE / 2 + FOREGROUND_RADIUS * sin(radians(10))
        ),
        (
            SIZE / 2 - 3.5 * STROKE,
            FOREGROUND_BBOX[1][1]
        )
    ],
    FOREGROUND_COLOR,
    STROKE
)
drawing.line(
    [
        (
            SIZE / 2 - FOREGROUND_RADIUS * sin(radians(25)),
            SIZE / 2 + FOREGROUND_RADIUS * sin(radians(10))
        ),
        (
            SIZE / 2 - FOREGROUND_RADIUS * sin(radians(25)),
            SIZE / 2 + FOREGROUND_RADIUS * cos(radians(25)) + STROKE
        )
    ],
    FOREGROUND_COLOR,
    STROKE
)


# Draw the 'J'.
drawing.arc(FOREGROUND_BBOX, 20, 80, FOREGROUND_COLOR, STROKE) 
drawing.line(
    [
        (
            SIZE / 2 + 2 * STROKE,
            SIZE / 2 + FOREGROUND_RADIUS * sin(radians(20))
        ),
        (
            SIZE / 2 + FOREGROUND_RADIUS * cos(radians(20)),
            SIZE / 2 + FOREGROUND_RADIUS * sin(radians(20))
        )
    ],
    FOREGROUND_COLOR,
    STROKE
)
drawing.line(
    [
        (
            SIZE / 2 + 2 * STROKE,
            SIZE / 2 + FOREGROUND_RADIUS * sin(radians(10))
        ),
        (
            SIZE / 2 + FOREGROUND_RADIUS * cos(radians(10)),
            SIZE / 2 + FOREGROUND_RADIUS * sin(radians(10))
        )
    ],
    FOREGROUND_COLOR,
    STROKE
)


# Clean up the edges.
drawing.arc([(0, 0), (SIZE, SIZE)], 0, 360, BACKGROUND_COLOR, STROKE)


# Display and save the image.
avatar.save('avatar.png')

