//Dont change it
requirejs(['ext_editor_io', 'jquery_190', 'raphael_210'],
    function (extIO, $) {
        function fusedCubesAnimation(tgt_node, data) {

            if (!data || !data.ext) {
                return
            }

            const input = data.in
            const explanation = data.ext.explanation
            const answer = data.ext.answer

            /*----------------------------------------------*
            *
            * attr
            *
            *----------------------------------------------*/
            const attr = {
                cube: {
                    blue: {
                        dark: {
                            'stroke-width': 0.5,
                            'stroke-width': 0,
                            'fill': '#0E81B3',
                        },
                        mid: {
                            'stroke-width': 0.5,
                            'stroke-width': 0,
                            'fill': '#38B8EE',
                        },
                        light: {
                            'stroke-width': 0.5,
                            'stroke-width': 0,
                            'fill': '#68C9F2',
                        },
                    },
                    orange: {
                        dark: {
                            'stroke-width': 0.5,
                            'stroke-width': 0,
                            'fill': '#F0801A',
                        },
                        mid: {
                            'stroke-width': 0.5,
                            'stroke-width': 0,
                            'fill': '#F4A561',
                        },
                        light: {
                            'stroke-width': 0.5,
                            'stroke-width': 0,
                            'fill': '#F7C091',
                        },
                    },
                },
                axis: {
                    normal: {
                        'stroke-width': '0.6px',
                        'stroke': '#294270',
                    },
                    arrow_end: {
                        'stroke-width': '0.6px',
                        'stroke': '#294270',
                        'arrow-end': 'block-wide-long',
                    },
                },
            };

            /*----------------------------------------------*
            *
            * values
            *
            *----------------------------------------------*/
            const EDGE = 13

            /*----------------------------------------------*
            *
            * make_cube (function)
            *
            *----------------------------------------------*/
            function make_cubes(x, y, z, e) {
                let cubes = []
                for (let dx = 0; dx < e; dx += 1) {
                    for (let dz = 0; dz < e; dz += 1) {
                        cubes.push(['orange', x + dx, y + (e - 1), z + dz, 1])
                    }
                }
                for (let dx = 0; dx < e; dx += 1) {
                    for (let dy = 0; dy < e - 1; dy += 1) {
                        cubes.push(['orange', x + dx, y + dy, z, 1])
                    }
                }
                for (let dz = 1; dz < e; dz += 1) {
                    for (let dy = 0; dy < e - 1; dy += 1) {
                        cubes.push(['orange', x + (e - 1), y + dy, z + dz, 1])
                    }
                }
                return cubes
            }

            /*----------------------------------------------*
            *
            * paper
            *
            *----------------------------------------------*/
            let max_px_size = 0
            let max_coord = 10
            let sizes = []
            const height = EDGE / 2
            const base = (EDGE / 2) * Math.sqrt(3)
            input.forEach(([x, y, z, e]) => {
                max_coord = Math.max(...[max_coord, x, x + e, y, y + e, z, z + e].map(c => Math.abs(c)))
                const left = (x * base) + (z * base)
                const right = left + base * e * 2
                const bottom = (x * height) + (z * -height) + (y * -EDGE) + (e * height)
                const top = bottom - EDGE * e * 2
                sizes = sizes.concat([left, right, top, bottom].map(c => Math.abs(c)))
            })

            max_px_size = Math.max(...sizes.concat([EDGE * Math.max(12, max_coord + 2)]))

            const SCALE = EDGE * 12 / max_px_size
            const OFFSET = max_px_size * SCALE

            const paper_width = max_px_size * 2 * SCALE
            const paper_height = max_px_size * 2 * SCALE

            const paper = Raphael(tgt_node, paper_width, paper_height, 0, 0)

            /*----------------------------------------------*
            *
            * draw process
            *
            *----------------------------------------------*/
            const axis_units = [['origin', -1, -1, 0, 1]]

            for (let i = -(max_coord + 1); i <= max_coord; i += 1) {
                axis_units.push(['x_axis', i, 0, 0, 1])
                axis_units.push(['y_axis', 0, i, 0, 1])
                axis_units.push(['z_axis', 0, 0, i, 1])
            }

            const cubes = input.flatMap(a => make_cubes(...a))
            const all_cubes = [
                ...axis_units,
                ...cubes,
            ].sort(sort_cubes)

            for (let cube of all_cubes) {
                draw_cube(...cube)
            }

            /*----------------------------------------------*
            *
            * sort cubes
            *
            *----------------------------------------------*/
            function sort_cubes(a, b) {
                const [ac, ax, ay, az, ae] = a
                const [bc, bx, by, bz, be] = b
                if (ay > by) return 1
                if (ay < by) return -1
                if (ax > bx) return 1
                if (ax < bx) return -1
                if (az < bz) return 1
                if (az > bz) return -1
                return 0
            }

            /*----------------------------------------------*
            *
            * draw cube (and axis)
            *
            *----------------------------------------------*/
            function draw_cube(color, cx, cy, cz, _) {

                const edge = EDGE * SCALE
                const height = edge / 2
                const base = (edge / 2) * Math.sqrt(3)

                const x = (cx * base) + (cz * base) + OFFSET
                const y = (cx * height) + (cz * -height) + (cy * -edge) + OFFSET

                if (color == 'origin') {
                    paper.text(max_px_size * SCALE - 6, max_px_size * SCALE + 10, 0)

                } else if (color == 'y_axis') {
                    paper.path(['M', x, y, 'v', -edge]).attr(
                        cy == max_coord ? attr.axis.arrow_end : attr.axis.normal)
                    if (cy == max_coord) {
                        paper.text(x - 7, y - edge, 'y').attr({ 'font-size': 10 })
                    }

                } else if (color == 'x_axis') {
                    paper.path(['M', x, y, 'l', base, height]).attr(
                        cx == max_coord ? attr.axis.arrow_end : attr.axis.normal)
                    if (cx == max_coord) {
                        paper.text(x + base, y + height - 8, 'x').attr({ 'font-size': 10 })
                    }

                } else if (color == 'z_axis') {
                    paper.path(['M', x, y, 'l', base, -height]).attr(
                        cz == max_coord ? attr.axis.arrow_end : attr.axis.normal)
                    if (cz == max_coord) {
                        paper.text(x + base, y - height - 8, 'z').attr({ 'font-size': 10 })
                    }

                } else {
                    // draw cube

                    // top
                    paper.path(['M', x, y - edge,
                        'l', base, -height,
                        'l', base, height,
                        'l', -base, height, 'z']).attr(attr.cube[color].mid)

                    // left
                    paper.path(['M', x, y,
                        'v', -edge,
                        'l', base, height,
                        'v', edge, 'z']).attr(attr.cube[color].light)

                    // right
                    paper.path(['M', x + base, y + height,
                        'l', base, -height,
                        'v', -edge,
                        'l', -base, height, 'z']).attr(attr.cube[color].dark)
                }
            }
        }

        var $tryit;

        var io = new extIO({
            multipleArguments: false,
            functions: {
                python: 'fused_cubes',
                js: 'fusedCubes'
            },
            animation: function ($expl, data) {
                fusedCubesAnimation(
                    $expl[0],
                    data,
                );
            }
        });
        io.start();
    }
);
