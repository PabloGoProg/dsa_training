for dir in */; do
  dir_name=$(basename "$dir")
  base_name=$(echo "$dir_name" | sed 's/^[0-9]*_//')
  [ ! -f "$dir/${base_name}.py" ] && touch "$dir/${base_name}.py"
  [ ! -f "$dir/problem_statement.md" ] && touch "$dir/problem_statement.md"
done