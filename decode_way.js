function numDecodings(s) {
    const solution = new Array(s.length).fill(-1)
    let a = backtracking(s, 0, solution)
}

function backtracking(s, starting_index, memoization) {
    let l = s.length

    if (starting_index >= l) {
        return 1
    }

    if (memoization[starting_index] !== -1) {
        return memoization[starting_index]
    }

    if (s[starting_index] === "0") {
        memoization[starting_index] = 0
        return 0
    }

    let result = backtracking(s, starting_index + 1, memoization)

    if (starting_index + 1 < l && // 두 자리인지 체크
        (s[starting_index] === "1" || // 첫째 자리가 1인지 체크
            (s[starting_index] === "2" && s[starting_index + 1] <= "6")) // 첫째 자리가 1이고, 둘째 자리가 6이하 인지 체크
    ) {
        result += backtracking(s, starting_index + 2, memoization)
    }

    memoization[starting_index] = result

    return result
}

console.log(numDecodings("127"))