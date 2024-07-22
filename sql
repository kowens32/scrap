cur.execute("""
                    INSERT INTO incidents (
                        sys_id, number, state, urgency, severity, category,
                        subcategory, opened_at, short_description, description
                    )
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT (sys_id) DO UPDATE
                    SET number = EXCLUDED.number,
                        state = EXCLUDED.state,
                        urgency = EXCLUDED.urgency,
                        severity = EXCLUDED.severity,
                        category = EXCLUDED.category,
                        subcategory = EXCLUDED.subcategory,
                        opened_at = EXCLUDED.opened_at,
                        short_description = EXCLUDED.short_description,
                        description = EXCLUDED.description
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