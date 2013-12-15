﻿module Main

open System
open MatrixMultiplicator

let measureTime f = 
    let time1 = System.DateTime.Now
    f() |> ignore
    let time2 = System.DateTime.Now
    time2 - time1

let printMatrix (m : int array array) =
    for i in 0..(m.Length - 1) do
        m.[i] |> printfn "%A"    

let multiplyMatrix (m1 : int array array) (m2 : int array array) =
    let n = m1.Length
    let arr = Array2D.zeroCreate n n
    for i in 0..(n - 1) do
        for j in 0..(n - 1) do
            Array2D.set arr i j (List.fold (fun acc k -> acc + m1.[i].[k] * m2.[k].[j]) 0 [0..(n - 1)])
    arr

let n = 1024
let m1 = new Matrix(n)
let m2 = new Matrix(n)

for threads in List.rev [for i in 0..5 -> int (Math.Pow(2., (float) i))] do
    let monad() = m1.Mult(m2, threads)
    measureTime monad |> printfn "Count threads: %i; Time: %A" threads

