import maya.cmds as mc
import maya.mel as mel

""" generate custom aovs for redshift """


def aov_generator():
    aovs = ['Cryptomatte', 'Depth', 'Depth', 'Diffuse Lighting', 'Global Illumination', 'Motion Vectors',
            'Reflections', 'Specular Lighting']  # AOV's to generate

    customnames = ['CP', 'Z_AA', 'Z_A', 'DIR', 'GI', 'MV', 'RFL', 'SPEC']

    def generate_aov(aov):
        """ generate aovs"""
        for word in aov:
            mc.rsCreateAov(type=word)

    generate_aov(aovs)

    def name_change(aovlist):
        """ give custom names to aovs in aovlist"""
        clean_names = []

        for word in aovlist:  # remove spaces between each word and
            clean = word.replace(' ', '')
            clean_names.append(clean)

        clean_names[2] = 'Depth1'  # REPLACE THE SECOND DEPTH AOV TO NOT HAVE DUPLICATES
        return clean_names

    def set_attributes(aovs, customnames):
        """ sets the attributes for the custom aovs"""

        for index, value in enumerate(aovs):  # CHANGE NAMES OF AOVLIST WITH CUSTOM NAMES
            mc.setAttr('rsAov_{}.name'.format(value), "{}".format(customnames[index]), type="string")
            if value == 'Depth':
                mc.setAttr('rsAov_Depth.depthMode', 2)  # depth-mode to 'inverted'
                mc.setAttr('rsAov_Depth.useCameraNearFar', 0)  # disable 'camera Near/Far'

            elif value == 'Depth1':
                mc.setAttr('rsAov_Depth1.depthMode', 2)  # depth-mode to 'inverted'
                mc.setAttr('rsAov_Depth1.useCameraNearFar', 0)  # disable 'camera Near/Far'
                mc.setAttr('rsAov_Depth1.filterMode', 1)  # filter mode to 'min-depth'

            elif value == 'MotionVectors':
                mc.setAttr('rsAov_MotionVectors.outputRawVectors', 1)  # output raw vectors
                mc.setAttr('rsAov_MotionVectors.filtering', 0)  # disable filtering

        mel.eval("redshiftUpdateActiveAovList()")  # refresh the redshift UI
        mc.confirmDialog(title='Generated', message='Redshift custom AOV\'s are generated')

    # call function
    return set_attributes(name_change(aovs), customnames)



