from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from pathlib import Path

class Command(BaseCommand):
    """Initialize database with migrations and sample data"""
    help = 'Initialize database with migrations and create admin user'

    def add_arguments(self, parser):
        parser.add_argument(
            '--username',
            type=str,
            default='admin',
            help='Admin username (default: admin)'
        )
        parser.add_argument(
            '--email',
            type=str,
            default='admin@example.com',
            help='Admin email (default: admin@example.com)'
        )
        parser.add_argument(
            '--password',
            type=str,
            default='admin123',
            help='Admin password (default: admin123)'
        )

    def handle(self, *args, **options):
        username = options['username']
        email = options['email']
        password = options['password']

        # Run migrations (NO TRANSACTION — REQUIRED FOR SQLITE)
        self.stdout.write(self.style.SUCCESS('[1/3] Running migrations...'))
        from django.core.management import call_command
        try:
            call_command('migrate', verbosity=1)
            self.stdout.write(self.style.SUCCESS('✓ Migrations completed'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'✗ Migrations failed: {e}'))
            return

        # Create superuser
        self.stdout.write(self.style.SUCCESS('[2/3] Creating admin user...'))
        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.WARNING(f'⚠ User "{username}" already exists'))
        else:
            try:
                User.objects.create_superuser(username=username, email=email, password=password)
                self.stdout.write(self.style.SUCCESS(f'✓ Admin user created: {username}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'✗ Failed to create admin user: {e}'))
                return

        # Create uploads directory
        self.stdout.write(self.style.SUCCESS('[3/3] Setting up directories...'))
        try:
            uploads_dir = Path(__file__).resolve().parent.parent.parent.parent / 'uploads'
            uploads_dir.mkdir(exist_ok=True)
            self.stdout.write(self.style.SUCCESS('✓ Uploads directory ready'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'✗ Failed to create uploads directory: {e}'))
            return

        self.stdout.write('\n' + '=' * 60)
        self.stdout.write(self.style.SUCCESS('Database initialization completed successfully!'))
        self.stdout.write('=' * 60)
        self.stdout.write('\nAdmin credentials:')
        self.stdout.write(f'  Username: {username}')
        self.stdout.write(f'  Email: {email}')
        self.stdout.write('\nNext: python manage.py runserver')
        self.stdout.write('=' * 60 + '\n')
