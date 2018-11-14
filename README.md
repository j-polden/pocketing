# pypocketing: ALPHA

Fill 2D regions with traversals, useful someday for generating milling tool paths.

## Disclaimer: Crusty Alpha Software
This is a dump of a bunch of prototype code. It is only put up in the hopes that it becomes less terrible someday, but until then you should probably use something else: [pyactp](https://github.com/mikedh/pyactp), [openvoronoi](https://github.com/aewallin/openvoronoi), [opencamlib](https://github.com/aewallin/opencamlib), [libarea](https://github.com/Heeks/libarea)


## Design Goals: Why Bother

There are a lot of other options above. However, most of them aren't super active and are generally C- based with python bindings. This is intended as a vectorized numpy approach to the same problem, in the vein of [trimesh](https://github.com/mikedh/trimesh)

*Scope:*
- Accept shapely.geometry.Polygon objects as input
- Generally, toolpath output is a sequence of (n, 2) float arrays
  - A sequence split indicates you can't go straight from one path to the other
- Should 