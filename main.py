from new_person import writing_down as wd
import view

t_book = {}
t_book = wd(t_book)
view.export_book(t_book)
view.print_dict(t_book)