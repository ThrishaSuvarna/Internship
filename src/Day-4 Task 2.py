raw_logs = ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]


unique_users = set(raw_logs)


is_id05_present = "ID05" in unique_users


print("Unique User IDs:", unique_users)
print("Is ID05 present?", is_id05_present)


print("Total log entries:", len(raw_logs))
<<<<<<< HEAD
print("Unique visitors:", len(unique_users))
=======
print("Unique visitors:", len(unique_users))
>>>>>>> f49fd9c9f786cd21697a7a890c46cae5bcfc5ce6
