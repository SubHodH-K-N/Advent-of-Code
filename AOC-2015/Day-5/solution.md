# Solution for Part I

`cat input | grep ".*[aeiou].*[aeiou].*[aeiou].*" | grep "\(.\)\1" | egrep -v "(ab|cd|pq|xy)" | wc -l`

# Solution for Part II

`cat input | grep "\(..\).*\1" | grep "\(.\).\1" | wc -l`
