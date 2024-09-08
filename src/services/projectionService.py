import numpy as np
from services.boxService import BoxService
from services.camService import CamService
from services.coneService import ConeService
from services.pipeService import PipeService
from services.coneTrunkService import ConeTrunkService
from services.cupService import CupService
from services.plot2dImageService import Plot2dImageService

class ProjectionService:    
    def generate_image():
        z_proj = 1
        n = 3
        f = 5
        aspect = 1920/1080

        p_m = [[z_proj/aspect, 0, 0, 0],
               [0, z_proj, 0, 0],
               [0, 0, (n+f)/(n-f), (2*n*f)/(n-f)],
               [0, 0, -1, 0]]

        points = []
        box = BoxService.add_box(points, False)
        cone = ConeService.add_cone(points, False)
        pipe = PipeService.add_pipe(points, False)
        cup = CupService.add_cup(points, False)
        coneTrunk = ConeTrunkService.add_coneTrunk(points, False)

        V = CamService.get_coordinate_system()
        
        box_by_v = np.dot(V, box)
        cone_by_v = np.dot(V, cone)
        pipe_by_v = np.dot(V, pipe)
        cup_by_v = np.dot(V, cup)
        coneTrunk_by_v = np.dot(V, coneTrunk)
        
        box_ = np.dot(p_m, box_by_v)
        cone_ = np.dot(p_m, cone_by_v)
        pipe_ = np.dot(p_m, pipe_by_v)
        cup_ = np.dot(p_m, cup_by_v)
        coneTrunk_ = np.dot(p_m, coneTrunk_by_v)

        mean_box = np.mean(box_, axis = 1)
        mean_cone = np.mean(cone_, axis = 1)
        mean_pipe = np.mean(pipe_, axis = 1)
        mean_cup = np.mean(cup_, axis = 1)
        mean_coneTrunk = np.mean(coneTrunk_, axis = 1)

        arr = dict({
            mean_cone[2]: box_,
            mean_box[2]: cone_,
            mean_pipe[2]: pipe_,
            mean_cup[2]: cup_,
            mean_coneTrunk[2]: coneTrunk_,
            })

        x = sorted(arr.items())

        arr = []

        for i in x:
            arr.append(i[1])


        return Plot2dImageService.plotImage_2d(arr)