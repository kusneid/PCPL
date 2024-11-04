let FuncVar first second third =
    let a = unbox first
    let b = unbox second
    let c = unbox third
    (a, b, c)

let SumInt (a: int, b: int, c: int) = a + b + c
let SumFloat (a: float, b: float, c: float) = a + b + c
let SumString (a: string, b: string, c: string) = a + b + c

let FuncList _ : (int * int * int) array =
    let arr = [| 1, 2, 5, 6, 13, 7, 8 |]
    let arr2 =
        [| for x in [ 1..10 ] do
               if x % 2 = 0 then
                   yield (x, x * x, x * x * x) |]
    arr2

let SecondTry =
    [| for x in [ 1..10 ] do
           if x % 2 = 0 then
               yield (x, x * x, x * x * x) |]

let rec Func2_1 (arr: int list) : int list =
    if arr.IsEmpty then
        []
    else
        (arr.Head * arr.Head) :: Func2_1(arr.Tail)

let rec Func2_2 =
    function
    | [] -> []
    | x :: xs -> x * x :: Func2_2 xs

let FuncList1 (arr: int list) : int list =
    let res: int list =
        arr
        |> List.map (fun x -> x * 2)
        |> List.sort
        |> List.filter (fun x -> x % 2 = 1)
    res

let FuncList2 (arr: int list) : int list =
    let operation =
        List.map (fun x -> x * 2) >> List.sort >> List.filter (fun x -> x % 2 = 1)
    let res = operation arr
    res

let FuncList3 (arr1: int list, arr2: int list) : (int * int) list =
    let res = List.zip arr1 arr2
    res

let main argv =
    let result1 = FuncVar (box 1) (box 2.5) (box "wfe")
    printfn "%A" result1

    let result2 = SumInt(1, 3, 2)
    printfn "%A" result2

    let result3 = SumFloat(1.0, 3.0, 2.0)
    printfn "%A" result3

    let result4 = SumString("a", "b", "c")
    printfn "%A" result4

    let result5 = FuncList()
    printfn "%A" result5

    let result6 = SecondTry
    printfn "%A" result6

    let result7 = Func2_1([ 1..7 ])
    printfn "%A" result7

    let result8 = Func2_2([ 1..7 ])
    printfn "%A" result8

    let result9 = FuncList1([ 1..7 ])
    printfn "%A" result9

    let result10 = FuncList2([ 1..7 ])
    printfn "%A" result10

    let result11 = FuncList3([ 1..7 ], [ 1..7 ])
    printfn "%A" result11

    0

main []
