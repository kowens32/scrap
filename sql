cur.execute("""
                    INSERT INTO incidents (
                        sys_id, number, state, urgency, severity, category,
                        subcategory, opened_at, short_description, description
                    )
                    VALUES (incident["sys_id"],incident["number"], incident["state"], incident["urgency"], incident["severity"], incident["category"], incident["subcategory"], incident["opened_at"], incident["short_description"], incident["description"])
                    ON CONFLICT (sys_id) DO UPDATE
                """, (
                    incident["sys_id"], incident["number"], incident["state"],
                    incident["urgency"], incident["severity"], incident["category"],
                    incident["subcategory"], incident["opened_at"],
                    incident["short_description"], incident["description"]
                ))
            conn.commit()
            print(f"Inserted {len(incidents)} incidents into the database")
        except psycopg2.Error as e:
            print(f"Error inserting incidents: {e}")
