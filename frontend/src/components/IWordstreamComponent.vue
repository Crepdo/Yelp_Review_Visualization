<template>
    <svg ref="word_svg" :width="svgWidth" :height="svgHeight">
        <!-- <g ref="star_svg"></g> -->
    </svg>
</template>

<script>
import * as d3 from "d3";
import * as d3fetch from "d3-fetch";
import * as d3collection from "d3-collection";
export default {
    name: "IWordstreamComponent",
    props: {
        svgWidth: {
            type: Number,
            required: true
        },
    },
    computed: {
        svgHeight() {
            return this.svgWidth / 1.61803398875;
        },
        gWidth() {
            return this.svgWidth - this.svgMargin.left - this.svgMargin.right;
        },
        gHeight() {
            return this.svgHeight - this.svgMargin.top - this.svgMargin.bottom;
        },
    },
    data: () => ({
        svgMargin: { top: 10, right: 30, bottom: 60, left: 60 },
        config: {
            topWord: 20,
            minFont: 10,
            maxFont: 30,
            tickFont: 12,
            legendFont: 12,
            curve: d3.curveMonotoneX
        },
    }),
    mounted() {
        d3fetch.json("/api/ind/word/").then((words_data) => {
            this.draw_stream(words_data);
            var svg = d3.select(this.$refs.word_svg).attr("width", this.svgWidth)
                .attr("height", this.svgHeight);
            this.wordstream(svg, words_data, this.config, this.svgWidth, this.svgHeight);
        });
    },
    methods: {
        draw_stream(words_data) {
            console.log(words_data);
        },
        wordstream(x, R, y, www, hhh) {
            d3.wordstreamLayout = function () {
                function H(a) {
                    var b = Object.keys(a[0].words), c = 0, e = Number.MAX_SAFE_INTEGER;
                    d3.map(
                        a, function (a) {
                            d3.map(b, function (b) {
                                var t = d3.max(
                                    a.words[b], function (a) {
                                        return a.frequency
                                    });
                                b = d3.min(
                                    a.words[b], function (a) {
                                        return a.frequency
                                    });
                                c < t && (c = t); e > b && (e = b)
                            })
                        });
                    I = c; Q = e;
                    L.domain([Q, I]).range([u, D])
                }
                function E(a) {
                    var b = z(a), c = 0;
                    d3.map(
                        b, function (a) {
                            var e = 0; Object.keys(b[0]).forEach(
                                function (b) { e += a[b] });
                            e > c && (c = e)
                        });
                    v.domain([0, c]).range([0, p[1]])
                }
                function A(a) {
                    var c = z(a), t = Object.keys(a[0].words), e = {}, d = ~~(p[0] / a.length), g = [];
                    t.forEach(
                        function (a) {
                            var b = [], e = {}; b.push((e.x = 0, e[a] = v(c[0][a]), e));
                            c.forEach(
                                function (c, e) {
                                    var f = {}; b.push((f.x = e * d + (d >> 1), f[a] = v(c[a]), f))
                                });
                            e = {};
                            b.push((e.x = p[0], e[a] = v(c[c.length - 1][a]), e));
                            g.push(b)
                        });
                    var q = [];
                    for (e = { $jscomp$loop$prop$i$8: 0 };
                        e.$jscomp$loop$prop$i$8 < g[0].length;
                        e = { $jscomp$loop$prop$i$8: e.$jscomp$loop$prop$i$8 }, e.$jscomp$loop$prop$i$8++)
                        q[e.$jscomp$loop$prop$i$8] = { x: g[0][e.$jscomp$loop$prop$i$8].x },
                            b.forEach(function (a) {
                                return function (b, c) {
                                    q[a.$jscomp$loop$prop$i$8] = Object.assign(q[a.$jscomp$loop$prop$i$8],
                                        g[c][a.$jscomp$loop$prop$i$8])
                                }
                            }(e));
                    var f = d3.stack().keys(b).offset(d3.stackOffsetWiggle)(q),
                        l = {},
                        h = d3.min(f[0], function (a) { return a[0] });
                    f.forEach(function (a) {
                        a.forEach(function (a) { a[0] -= h; a[1] -= h })
                    });
                    t.forEach(function (a, b) {
                        l[a] = [];
                        for (var c = 1; c < f[b].length - 1; c++)
                            l[a].push({
                                x: f[b][c].data.x - (d >> 1),
                                y: f[b][c][0],
                                width: d,
                                height: f[b][c][1] - f[b][c][0]
                            })
                    });
                    return e = {
                        topics: t, data: a, layers: f,
                        innerBoxes: l
                    }
                }
                function w(a, b) {
                    var c = ~~Math.sqrt(b.boxWidth * b.boxWidth + b.boxHeight * b.boxHeight),
                        e = ~~(b.boxX + (b.boxWidth * (Math.random() + .5) >> 1)),
                        d = ~~(b.boxY + (b.boxHeight * (Math.random() + .5) >> 1)),
                        g = O([b.boxWidth, b.boxHeight]), q = .5 > Math.random() ? 1 : -1,
                        f = -q, l;
                    a.x = e; a.y = d;
                    for (a.placed = !1; l = g(f += q);) {
                        var h = ~~l[0]; l = ~~l[1];
                        if (Math.max(Math.abs(h), Math.abs(l)) >= c)
                            break;
                        a.x = e + h; a.y = d + l;
                        if (!(0 > a.x + a.x0
                            || 0 > a.y + a.y0
                            || a.x + a.x1 > p[0]
                            || a.y + a.y1 > p[1]
                            || F(a, b))) {
                            x(a, b); a.placed = !0;
                            break
                        }
                    }
                }
                function F(a, b) {
                    for (var c = a.height,
                        e = a.width, d = b.width, g = 0; g < c; g++)
                        for (var q = 0; q < e; q++) {
                            var f = a.sprite[g * e + q];
                            if (0 != b.sprite[(g + a.y + a.y0) * d + q + (a.x + a.x0)] && 0 != f)
                                return !0
                        }
                    return !1
                }
                function x(a, b) {
                    for (var c = a.y + a.y0, e = a.x + a.x0, d = b.width, g = a.width, q = a.height, f = 0;
                        f < q;
                        f++)
                        for (var l = 0; l < g; l++) {
                            var h = f * g + l, m = (f + c) * d + l + e;
                            0 != a.sprite[h] && (b.sprite[m] = a.sprite[h])
                        }
                }
                function y(a, b) {
                    // streamPath1 = [];
                    // streamPath2 = [];
                    var c = p[0], e = p[1];
                    c = d3.select(document.createElement("svg")).attr("width", c).attr("height", e);
                    var d = c.append("g"), g = a.topics.indexOf(b),
                        h = d3.area().curve(G).x(function (a) { return a.data.x })
                            .y0(0)
                            .y1(function (a) { return a[0] });
                    e = d3.area().curve(G).x(function (a) { return a.data.x })
                        .y0(function (a) { return a[1] }).y1(e);
                    d.append("path").datum(a.layers[g]).attr("d", h)
                        .attr("stroke", "red").attr("stroke-width", 2)
                        .attr("fill", "red").attr("id", "path1");
                    d.append("path").datum(a.layers[g])
                        .attr("d", e).attr("stroke", "red")
                        .attr("stroke-width", 2).attr("fill", "red")
                        .attr("id", "path2");
                    return c
                }
                function M(a, b) {
                    var c = y(a, b), e = c.select("#path1").attr("d");
                    e = new Path2D(e);
                    c = c.select("#path2").attr("d");
                    c = new Path2D(c);
                    var d = document.createElement("canvas");
                    d.width = p[0]; d.height = p[1];
                    var g = d.getContext("2d");
                    g.fillStyle = "red"; g.fill(e); g.fill(c);
                    return d;
                }
                function J(a, b) {
                    var c = M(a, b), e = c.width, d = c.height, g = { x: 0, y: 0 };
                    g.width = e; g.height = d;
                    for (var h = [], f = 0; f < e * d; f++)
                        h[f] = 0;
                    c = c.getContext("2d").getImageData(0, 0, e, d).data;
                    for (f = 0; f < e * d; f++)
                        h[f] = c[f << 2]; g.sprite = h;
                    return g;
                }
                function N(a) {
                    a.width = 4096; a.height = 4096; a = a.getContext("2d");
                    a.fillStyle = a.strokeStyle = "red"; a.textAlign = "center";
                    a.textBaseline = "middle";
                    return a;
                }
                function B(a) {
                    var b = K.includes("a") ? 15 : 0, c = a.data, e = N(document.createElement("canvas"));
                    e.clearRect(0, 0, 4096, 4096);
                    for (var d = 0, g = 0, q = 0, f = { $jscomp$loop$prop$i$10: 0 };
                        f.$jscomp$loop$prop$i$10 < c.length;
                        f = { $jscomp$loop$prop$i$10: f.$jscomp$loop$prop$i$10 }, f.$jscomp$loop$prop$i$10++)
                        a.topics.forEach(function (a) {
                            return function (f) {
                                f = c[a.$jscomp$loop$prop$i$10].words[f];
                                for (var l = f.length, m = -1, k; ++m < l;) {
                                    k = f[m]; e.save(); k.fontSize = ~~L(k.frequency);
                                    k.rotate = (~~(4 * Math.random()) - 2) * b; e.font = ~~(k.fontSize + 1) + "px " + C;
                                    var n = ~~e.measureText(k.text).width, t = k.fontSize;
                                    if (k.rotate) {
                                        var p = Math.sin(k.rotate * h), r = Math.cos(k.rotate * h),
                                            u = n * r, I = n * p;
                                        r *= t; n = t * p; n = ~~Math.max(Math.abs(u + n), Math.abs(u - n));
                                        t = ~~Math.max(Math.abs(I + r), Math.abs(I - r))
                                    }
                                    t > q && (q = t);
                                    4096 <= d + n && (d = 0, g += q, q = 0);
                                    if (4096 <= g + t) break;
                                    e.translate(d + (n >> 1), g + (t >> 1));
                                    k.rotate && e.rotate(k.rotate * h);
                                    e.fillText(k.text, 0, 0);
                                    k.padding && (e.lineWidth = 2 * k.padding, e.strokeText(k.text, 0, 0));
                                    e.restore();
                                    k.width = n;
                                    k.height = t;
                                    k.x = d;
                                    k.y = g;
                                    k.x1 = n >> 1;
                                    k.y1 = t >> 1;
                                    k.x0 = -k.x1;
                                    k.y0 = -k.y1;
                                    k.timeStep = a.$jscomp$loop$prop$i$10;
                                    k.streamHeight = v(k.frequency); d += n
                                }
                            }
                        }(f));
                    for (f = { $jscomp$loop$prop$bc$12: 0 };
                        f.$jscomp$loop$prop$bc$12 < c.length;
                        f = { $jscomp$loop$prop$bc$12: f.$jscomp$loop$prop$bc$12 }, f.$jscomp$loop$prop$bc$12++)
                        a.topics.forEach(function (a) {
                            return function (b) {
                                b = c[a.$jscomp$loop$prop$bc$12].words[b];
                                for (var d = b.length, f = -1, g; ++f < d;) {
                                    g = b[f];
                                    var h = e.getImageData(g.x, g.y, g.width, g.height).data;
                                    g.sprite = [];
                                    for (var n = 0; n << 2 < h.length; n++)
                                        g.sprite.push(h[n << 2])
                                }
                            }
                        }(f)); return e.getImageData(0, 0, 4096, 4096)
                }
                function z(a) {
                    var b = Object.keys(a[0].words), c = [];
                    d3.map(a, function (a) {
                        var e = {};
                        b.forEach(function (b) {
                            var c = 0; a.words[b].forEach(function (a) { c += a.frequency });
                            e[b] = c
                        });
                        c.push(e)
                    }); return c
                }
                function r(a) {
                    var b = a[0] / a[1];
                    return function (a) {
                        return [b * (a *= .1) * Math.cos(a), a * Math.sin(a)]
                    }
                }
                var m = [], p = [1200, 500], D = 24, u = 10, C = "Arial", K = "n",
                    L = d3.scaleLinear(), v = d3.scaleLinear(),
                    O = r, G = d3.curveMonotoneX, b = [], d = 10, c = {}, h = Math.PI / 180,
                    n, S, I, Q; c.boxes = function () {
                        m.forEach(function (a) { b.forEach(function (b) { a.words[b].splice(d) }) });
                        H(m);
                        E(m);
                        var a = A(m); B(a);
                        for (var c = 0; c < a.topics.length; c++)
                            for (var h = a.topics[c], e = J(a, h), n = a.innerBoxes[h], g = 0;
                                g < a.data.length;
                                g++) {
                                var q = a.data[g].words[h], f = q.length, l = n[g];
                                e.boxWidth = l.width;
                                e.boxHeight = l.height; e.boxX = l.x; e.boxY = l.y;
                                for (l = 0; l < f; l++)
                                    w(q[l], e)
                            }
                        return a
                    };
                var T = { achemedean: r, rectangular: function (a) { return function (a) { } } };
                c.getImageData = B; c.cloudCollide = F; c.place = w; c.buildSvg = y; c.buildCanvas = M;
                c.buildBoard = J; c.placeWordToBoard = x; c.buildBoxes = A; c.buildFontScale = H;
                c.curve = function (a) { return arguments.length ? (G = a, c) : G };
                var streamPath1 = [];
                var streamPath2 = [];
                c.streamPath1 = function (a) { return arguments.length ? (streamPath1 = a, c) : streamPath1 };
                c.streamPath2 = function (a) { return arguments.length ? (streamPath1 = a, c) : streamPath2 };
                c.font = function (a) { return arguments.length ? (C = a, c) : C };
                c.frequencyScale = function (a) { return arguments.length ? (v = a, c) : v };
                c.spiral = function (a) { return arguments.length ? (O = T[a] || a, c) : O };
                c.data = function (a) { return arguments.length ? (m = a, c) : m };
                c.size = function (a) { return arguments.length ? (p = a, c) : p };
                c.maxFontSize = function (a) { return arguments.length ? (D = a, c) : D };
                c.minFontSize = function (a) { return arguments.length ? (u = a, c) : u };
                c.minSud = function (a) { return arguments.length ? (S = a, c) : S };
                c.maxSud = function (a) { return arguments.length ? (n = a, c) : n };
                c.minFreq = function (a) { return arguments.length ? (Q = a, c) : Q };
                c.maxFreq = function (a) { return arguments.length ? (I = a, c) : I };
                c.fontScale = function (a) { return arguments.length ? (L = a, c) : L };
                c.font = function (a) { return arguments.length ? (C = a, c) : C };
                c.flag = function (a) { return arguments.length ? (K = a, c) : K };
                c.categories = function (a) { return arguments.length ? (b = a, c) : b };
                c.topWord = function (a) { return arguments.length ? (d = a, c) : d };
                return c
            };
            (function (H) {
                var E = www;
                var A = hhh;
                var w = y.minFont, F = y.maxFont, P = y.topWord, R = y.tickFont, M = y.legendFont, J = y.curve;
                var N = d3.scaleOrdinal(d3.schemeCategory10);
                var B = Object.keys(H[0].words);
                var z = x.append("g").attr("id", "axisGroup");
                var r = x.append("g").attr("id", "xGridlinesGroup");
                var m = x.append("g").attr("id", "main"),
                    p = x.append("g").attr("id", "legend"), D = B.length * M; E -= 40; A -= 60 + D;
                w = d3.wordstreamLayout().size([E, A]).fontScale(d3.scaleLinear())
                    .minFontSize(w).maxFontSize(F).data(H).categories(B).topWord(P).curve(J);
                var u = w.boxes();
                H = w.maxFreq(); w = w.minFreq();
                var C = d3.area().curve(J).x(function (b) { return b.data.x }).
                    y0(function (b) { return b[0] }).y1(function (b) { return b[1] }),
                    K = [];
                u.data.forEach(function (b) { K.push(b.date) });
                J = d3.min(u.layers[0], function (b) { return b[0] });
                F = d3.scaleBand().domain(K).rangeRound([0, E]);
                F = d3.axisBottom(F);
                z.attr("transform", "translate(20," + (A + 20 + 10 + D) + ")");
                (function (b) {
                    b.selectAll(".domain").attr("fill", "none").attr("stroke-opacity", 0);
                    b.selectAll(".tick line").attr("fill", "none").attr("stroke-opacity", 0);
                    b.selectAll(".tick text").attr("font-family", "serif").attr("font-size", R)
                })(z.call(F)
                    .selectAll("text")
                    .style("text-anchor", "end")
                    .style("font-size", "75%")
                    .attr("dx", "-.8em")
                    .attr("dy", ".15em")
                    .attr("transform", function (d) {
                        return "rotate(-45)";
                    }));
                z = d3.scaleBand().domain(d3.range(0, K.length + 1)).rangeRound([0, E + E / u.data.length]);
                z = d3.axisBottom(z);
                r.attr("transform",
                    "translate(" + (20 - E / u.data.length / 2) + "," + (A + 20 + 10 + D + 30) + ")");
                (function (b) {
                    b.selectAll(".domain").attr("fill",
                        "none").attr("stroke", "none");
                    b.selectAll(".tick line").attr("fill", "none").attr("stroke-width", .7)
                        .attr("stroke", "lightgray")
                })(r.call(
                    z.tickSize(-A - 10 - D - 30, 0, 0).tickFormat(""))
                );

                m.attr("transform", "translate(20," + (20 - J) + ")");
                var L = m.append("g").attr("id", "wordstreamG");
                r = m.selectAll(".curve").data(u.layers);
                r.exit().remove();
                r.enter().append("path").attr("d", C).style("fill",
                    function (b, d) { return N(d) })
                    .attr("class", "curve").attr("fill-opacity", 0).attr("stroke", "black")
                    .attr("stroke-width", 0).attr("topic", function (b, d) { return B[d] });
                r.attr("d", C).style("fill", function (b, d) { return N(d) }).attr("fill-opacity", 0)
                    .attr("stroke", "black").attr("stroke-width", 0)
                    .attr("topic", function (b, d) { return B[d] });
                var v = [];
                d3.map(u.data, function (b) { u.topics.forEach(function (d) { v = v.concat(b.words[d]) }) });
                var O = d3.scaleLog().domain([w, H]).range([.4, 1]);
                var G; r = m.selectAll(".word").data(v, function (b) { return b.id });
                r.exit().remove();
                r.enter().append("g").attr("transform", function (b) {
                    return "translate(" + b.x + ", " + b.y + ")rotate(" + b.rotate + ")"
                }).attr("class", "word").append("text").text(function (b) { return b.text })
                    .attr("id", function (b) { return b.id })
                    .attr("class", "textData").attr("font-family", "Arial")
                    .attr("font-size", function (b) { return b.fontSize })
                    .attr("fill", function (b, d) { return N(B.indexOf(b.topic)) })
                    .attr("fill-opacity", function (b) { return O(b.frequency) }).attr("text-anchor", "middle")
                    .attr("alignment-baseline", "middle").attr("topic", function (b) { return b.topic })
                    .attr("visibility", function (b) { return b.placed ? "visible" : "hidden" });

                r.attr("transform",
                    function (b) { return "translate(" + b.x + ", " + b.y + ")rotate(" + b.rotate + ")" })
                    .select("text").attr("font-size", function (b) { return b.fontSize })
                    .attr("visibility", function (b) { return b.placed ? "visible" : "hidden" });

                m.selectAll(".textData")
                    .on("mouseenter", function () {
                        var b = d3.select(this);
                        b.style("cursor", "pointer");
                        G = b.attr("fill");
                        var d = b.text(), c = b.attr("topic");
                        m.selectAll(".textData")
                            .filter(function (b) { return b && b.text === d && b.topic === c })
                            .attr("stroke", G).attr("stroke-width", 1)
                    });
                m.selectAll(".textData").on("mouseout",
                    function () {
                        var b = d3.select(this);
                        b.style("cursor", "default");
                        var d = b.text(), c = b.attr("topic");
                        m.selectAll(".textData")
                            .filter(function (b) { return b && !b.cloned && b.text === d && b.topic === c })
                            .attr("stroke", "none").attr("stroke-width", 0)
                    });
                m.selectAll(".textData").on("click", function () {
                    var b = d3.select(this), d = b.text(), c = b.attr("topic");
                    b = m.selectAll(".textData")
                        .filter(function (b) { return b && b.text === d && b.topic === c })
                        ._groups; var h = []; d3.select("path[topic='" + c + "']")
                            .data()[0].forEach(function (b, c) {
                                var d = [];
                                d[0] = b[1]; d[1] = b[1]; d.data = b.data; h.push(d)
                            });
                    b[0].forEach(function (b) {
                        var d = b.__data__, m = d.fontSize, n = h[d.timeStep + 1];
                        n[1] = n[0] - d.streamHeight; d = b.cloneNode(!0);
                        d3.select(d).attr("visibility", "visible").attr("stroke", "none").attr("stroke-size", 0);
                        var p = b.parentNode.cloneNode(!1);
                        p.appendChild(d); b.parentNode.parentNode.appendChild(p);
                        d3.select(p).attr("cloned", !0).attr("topic", c).transition().duration(300)
                            .attr("transform", function (a, b) {
                                return "translate(" + n.data.x + "," + (n[1] - m / 2) + ")"
                            })
                    });
                    h[0][1] = h[1][1];
                    h[h.length - 1][1] = h[h.length - 2][1];
                    L.append("path").datum(h).attr("d", C).style("fill", G)
                        .attr("fill-opacity", 1).attr("stroke", "black").attr("stroke-width", .3)
                        .attr("topic", c).attr("wordstream", !0);
                    m.selectAll(".textData").filter(function (b) { return b && !b.cloned && b.topic === c })
                        .attr("visibility", "hidden")
                });
                B.forEach(function (b) {
                    d3.select("path[topic='" + b + "']").on("click", function () {
                        m.selectAll(".textData")
                            .filter(function (d) { return d && !d.cloned && d.placed && d.topic === b })
                            .attr("visibility", "visible");
                        document.querySelectorAll("g[cloned='true'][topic='" + b + "']")
                            .forEach(function (b) { b.parentNode.removeChild(b) });
                        document.querySelectorAll("path[wordstream='true'][topic='" + b + "']")
                            .forEach(function (b) { b.parentNode.removeChild(b) })
                    })
                });
                p.attr("transform", "translate(20," + (A + 20 + 10) + ")");
                p = p.selectAll("g").data(u.topics).enter().append("g")
                    .attr("transform", function (b, d) { return "translate(10," + d * M + ")" });
                p.append("circle").attr("r", 5).attr("fill", function (b, d) { return N(d) })
                    .attr("fill-opacity", 1).attr("stroke", "black").attr("stroke-width", .5);
                p.append("text").text(function (b) { return b }).attr("font-size", M)
                    .attr("alignment-baseline", "middle").attr("dx", 8)
            })(R);
        }

    }
}
</script>

