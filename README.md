## What?
A custom Multipass AOV generator for redshift Maya

## Why?
To create a generalized AOV-format for every artists in the studio, this way there are no problems with different settings later on in the pipeline.

At the moment Redshift cannot save AOV settings, this script fixed this problem by setting up only onc., 
From now on you be able to generate them everytime you need it.

## How?
Inside Maya, copy the content of the script in the 'Script Editor'.
click 'Add to shelf' to keep it when restarting

Add your own custom AOV by adding it to the list `aovs`.

```
aovs = ['Cryptomatte', 'Depth', 'Diffuse Lighting', 'Global Illumination', 'Motion Vectors',
        'Reflections', 'Specular Lighting', 'INSERT HERE']  
```

When you add a new AOV and want to change it's settings, copy one of the statement and set the attributes by checking 
the MEL ECHOS from maya
```
elif value == 'INSERT AOV NAME':
    mc.setAttr('rsAov_MotionVectors.outputRawVectors', 1)  # output raw vectors
    mc.setAttr('rsAov_MotionVectors.filtering', 0)         # disable filtering
```

