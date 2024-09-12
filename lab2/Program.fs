let Func first second third =
    let a = unbox<int> first
    let b = unbox<float> second
    let c = unbox<string> third
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
//|>List.max

let FuncList2 (arr: int list) : int list =
    let operation =
        List.map (fun x -> x * 2) >> List.sort >> List.filter (fun x -> x % 2 = 1)
    //>> List.fold

    let res = operation arr
    res

let FuncList3 (arr1: int list, arr2: int list) : (int * int) list =
    let res = List.zip arr1 arr2
    res




let main argv =
    let result = FuncList3([ 1..7 ], [ 1..7 ]) //Func2_2([ 1..7 ]) //FuncList() //SecondTry  //SumFloat(1, 3, 2) //Func (box 1) (box 2.5) (box "wfe")
    printfn "%A" result
    0

main []
