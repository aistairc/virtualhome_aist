# VirtualHome-AIST

This is an extended VirtualHome based on VirtualHome v2.2 with some additional functions.

For more information about original VirtualHome v2.2, please see [here](https://github.com/xavierpuigf/virtualhome/tree/v2.2.0).

## What is New
* We added [actions](./simulation/README.md#supported-in-unity-simulator) that can be executed in the Unity simulator. That is, many motions not supported by the original VirtualHome can now be executed.
* Several new camera modes have been added.
* It is now possible to output JSON data in frame-by-frame.
* The 2D bounding boxes of objects can now be output.
* A convenient jupyter notebook is provided to run a large number of simulations based on the script data and save the results.

## How to use
### Download Unity Simulator
Download the VirtualHome UnitySimulator executable and move it under `simulation/unity_simulator`.

- [Download](https://github.com/aistairc/virtualhome_unity_aist/releases)

### Test simulator

To test the simulator in a local machine, double click the executable.

### Generating Videos and JSON data

* [VH Execution Notebooks](https://github.com/aistairc/virtualhome_aist/tree/main/demo)


## VirtualHome2KG

A framework to convert VirtualHome execution results into knowledge graphs.

For more information, please visit [**here**](https://github.com/aistairc/virtualhome2kg).

## Datasets

Datasets created using VirtualHome-AIST and VirtualHome2KG are available [**here**](https://github.com/KnowledgeGraphJapan/KGRC-RDF/blob/kgrc4si/README_en.md).

## Visualization

A visualization tool was developed to simultaneously check the generated videos and corresponding knowledge graphs.
* [https://github.com/aistairc/virtualhome2kg_visualization](https://github.com/aistairc/virtualhome2kg_visualization)

## VirtualHome-AIST Unity Source Code

Please visit [here](https://github.com/aistairc/virtualhome_unity_aist/).




