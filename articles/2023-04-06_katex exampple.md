---
title: Katex example
date: 2023-04-06T21:33:00+00:00
modified: 2023-05-26T16:00:00+00:00
tags: markdown, katex
slug: katex-example
author: CarlosJasso
summary: Test to verify that pelican parses basic markdown + katex.
status: published
---

# katex!

$$
    x + y = 50 \\
    x − y = 10
$$

$$
    \begin{bmatrix}
        \def\arraystretch{1.5}
            \begin{array}{cc|c}
                1 & 1 & 50 \\ 
                1 & -1 & 10 \\
        \end{array}
    \end{bmatrix}
$$

$$ D = \begin{bmatrix} 1 & 1 \\ 1 & -1 \\ \end{bmatrix} = (1)(-1)-(1)(1) = -2 $$

$$
    D_x = \begin{bmatrix} 50 & 1 \\ 10 & -1 \\ \end{bmatrix} = (50)(-1)-(1)(10) = -60
$$

$$
    x = \frac{D_x}{D} = \frac{-60}{-2} = 30
$$

$$
    D_y = \begin{bmatrix} 1 & 50 \\ 1 & 10 \\ \end{bmatrix} = (1)(10)-(50)(1) = -40
$$

$$
    y = \frac{D_y}{D} = \frac{-40}{-2} = 20
$$
