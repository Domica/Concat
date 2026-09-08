import re

path = "engine/crates/concat/src/studio.rs"
with open(path, 'r') as f:
    code = f.read()

# Dodaj limit nakon project_path
code = code.replace(
    'let project_path = session.path().to_owned();',
    '''let project_path = session.path().to_owned();

        const MAX_CONCURRENT_JOBS: usize = 2;
        let available_slots = MAX_CONCURRENT_JOBS.saturating_sub(self.art_pending.len());
        if available_slots == 0 {
            return;
        }'''
)

# Dodaj .take(available_slots) prije .collect()
code = re.sub(
    r'(\}\)\n)(\s+\.collect\(\);)',
    r'\1            .take(available_slots)\n\2',
    code,
    count=1
)

# Dodaj request_media_art() na kraj callback-a
code = code.replace(
    '''.retain(|key, _| !key.starts_with(&prefix));
                    }
                },''',
    '''.retain(|key, _| !key.starts_with(&prefix));
                    }
                    studio.request_media_art();
                },'''
)

with open(path, 'w') as f:
    f.write(code)
print("CPU fix applied.")
