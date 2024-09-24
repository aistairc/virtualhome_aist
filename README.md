# VirtualHome-AIST

This is an extended VirtualHome based on VirtualHome v2.2 with some additional functions.

For more information about original VirtualHome v2.2, please see [here](https://github.com/xavierpuigf/virtualhome/tree/v2.2.0).

## What is New
* We added [actions](./simulation/README.md#supported-in-unity-simulator) that can be executed in the Unity simulator. That is, many motions not supported by the original VirtualHome can now be executed.
* Several [new cameras](https://github.com/aistairc/virtualhome_unity_aist#addition-of-new-four-cameras) and three [new camera modes](https://github.com/aistairc/virtualhome_aist/tree/main/simulation/unity_simulator#modification-of-render_script-recorded-on-20230421) have been added.
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

To use the functions added by VirtualHome-AIST, please see here.
* [VH Execution Notebooks](https://github.com/aistairc/virtualhome_aist/tree/main/demo)


## VirtualHome2KG

A framework to convert VirtualHome execution results into knowledge graphs.

For more information, please visit [**here**](https://github.com/aistairc/virtualhome2kg).

## Datasets

Datasets created using VirtualHome-AIST and VirtualHome2KG are available [**here**](https://github.com/KnowledgeGraphJapan/KGRC-RDF/blob/kgrc4si/README.md).

## Visualization

A visualization tool was developed to simultaneously check the generated videos and corresponding knowledge graphs.
* [https://github.com/aistairc/virtualhome2kg_visualization](https://github.com/aistairc/virtualhome2kg_visualization)

## VirtualHome-AIST Unity Source Code

Please visit [here](https://github.com/aistairc/virtualhome_unity_aist/).


## Publication
Shusaku Egami, Takanori Ugai, Swe Nwe Nwe Htun, Ken Fukuda: "VHAKG: A Multi-modal Knowledge Graph Based on Synchronized Multi-view Videos of Daily Activities." Proceedings of the 33rd ACM International Conference on Information and Knowledge Management (CIKM2024), to appear, 2024.10 [[preprint](https://arxiv.org/abs/2408.14895)]

```
@InProceedings{egami24vhakg,
author="Shusaku Egami
and Takanori Ugai
and Swe Nwe Nwe Htun
and Ken Fukuda",
title="{VHAKG}: A Multi-modal Knowledge Graph Based on Synchronized Multi-view Videos of Daily Activities",
booktitle="Proceedings of the 33rd ACM International Conference on Information and Knowledge Management",
note="to appear",
year="2024",
doi="10.1145/3627673.3679175"
}
```


