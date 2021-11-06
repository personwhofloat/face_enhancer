import sys
sys.path[:1] = ["models/enhancement/GFPGAN",".."]
from GFPGAN import GFPGANer
sys.path[:1] = ["models/colorization/GPEN/",".."]
print(sys.path)
from GPEN import FaceColorization

