# this is models.py for companymaster (master tables)
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone


class PDFModel(models.Model):
    filename = models.CharField(max_length=255, null=False)
    path = models.CharField(max_length=255, null=False)

    def __str__(self):
        return f'{self.filename}'

    class Meta:
        verbose_name = "PDFModel"
        verbose_name_plural = "PDFModel"


class PDFPage(models.Model):
    pdf = models.ForeignKey(PDFModel, on_delete=models.PROTECT)
    page_no = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.page_no}'

    class Meta:
        verbose_name = "PDFPage"
        verbose_name_plural = "PDFPage"


class Filing(models.Model):
    original_link = models.CharField(
        max_length=255, verbose_name="Original Link")
    custom_link = models.CharField(max_length=255, verbose_name="Custom Link")
    file_name = models.CharField(
        max_length=255, null=False, verbose_name="File Name")
    report_date = models.DateTimeField(
        null=True, blank=True, editable=True, verbose_name="Report Date")
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(null=True, blank=True, editable=True)
    updated_by = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name="Updated By", blank=True, default=1)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.original_link}'

    class Meta:
        verbose_name = "Filing"
        verbose_name_plural = "Filings"


class Company(models.Model):
    company_name = models.CharField(max_length=255, null=False)
    company_name_pdf = models.ForeignKey(
        PDFPage, on_delete=models.PROTECT, null=True, related_name="company_name_pdf")
    symbol = models.CharField(max_length=255, null=False)
    symbol_pdf = models.ForeignKey(
        PDFPage, on_delete=models.PROTECT, null=True, related_name="symbol_pdf")
    exchange_pdf = models.ForeignKey(
        PDFPage, on_delete=models.PROTECT, null=True, related_name="exchange_pdf")
    country_pdf = business_description_pdf = models.ForeignKey(
        PDFPage, on_delete=models.PROTECT, null=True, related_name="country_pdf")
    address_pdf = business_description_pdf = models.ForeignKey(
        PDFPage, on_delete=models.PROTECT, null=True, related_name="address_pdf")
    cik = models.CharField(max_length=255, null=True, blank=True)
    cusip = models.CharField(max_length=255, null=True, blank=True)
    isin = models.CharField(max_length=255, null=True, blank=True)
    lei = models.CharField(max_length=255, null=True, blank=True)
    sedol = models.CharField(max_length=255, null=True, blank=True)
    mic_code = models.CharField(max_length=255, null=True, blank=True)
    mic_seg = models.CharField(max_length=255, null=True, blank=True)
    sic_code = models.CharField(max_length=255, null=True, blank=True)
    no_of_employees = models.IntegerField(null=True, blank=True)
    year_of_establishment = models.IntegerField(null=True, blank=True)
    financial_year_end = models.CharField(
        max_length=255, null=True, blank=True)
    business_description = models.CharField(
        max_length=1000, null=True, blank=True)
    business_description_pdf = models.ForeignKey(
        PDFPage, on_delete=models.PROTECT, null=True, related_name="business_description_pdf")
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(null=True, blank=True, editable=False)
    updated_by = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name="Updated By", blank=True, default=1)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"


class Currency(models.Model):
    currency_name = models.CharField(max_length=255, null=False)
    currency_short_name = models.CharField(max_length=255, null=False)
    currency_symbol = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(null=True, blank=True, editable=False)
    updated_by = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name="Updated By", blank=True, default=1)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.currency_short_name}'

    class Meta:
        verbose_name = "Currency"
        verbose_name_plural = "Currencies"


class Exchange(models.Model):
    exchange_name = models.CharField(max_length=255, null=False)
    exchange_short_name = models.CharField(max_length=255, null=False)
    exchange_symbol = models.CharField(max_length=255, null=False, blank=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(null=True, blank=True, editable=False)
    updated_by = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name="Updated By", blank=True, default=1)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.exchange_name}'

    class Meta:
        verbose_name = "Exchange"
        verbose_name_plural = "Exchanges"


class Country(models.Model):
    country_name = models.CharField(max_length=255, null=False)
    country_symbol = models.CharField(max_length=255, null=False)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(null=True, blank=True, editable=False)
    updated_by = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name="Updated By", blank=True, default=1)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.country_name}'

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"


class Industry(models.Model):
    industry_name = models.CharField(max_length=255, null=False)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(null=True, blank=True, editable=False)
    updated_by = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name="Updated By", blank=True, default=1)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.industry_name}'

    class Meta:
        verbose_name = "Industry"
        verbose_name_plural = "Industries"


class Fundparty(models.Model):
    company_name = models.CharField(max_length=255, null=False)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(null=True, blank=True, editable=False)
    updated_by = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name="Updated By", blank=True, default=1)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.company_name}'

    class Meta:
        verbose_name = "Fundparty"
        verbose_name_plural = "Fundparties"


class CompanyOfferings(models.Model):
    offering_type = models.CharField(max_length=255, null=False)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(null=True, blank=True, editable=False)
    updated_by = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name="Updated By", blank=True, default=1)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.offering_type}'

    class Meta:
        verbose_name = "CompanyOfferings"
        verbose_name_plural = "CompanyOfferings"


class OfferStatus(models.Model):
    offer_status = models.CharField(max_length=255, null=False)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(null=True, blank=True, editable=False)
    updated_by = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name="Updated By", blank=True, default=1)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.offer_status}'

    class Meta:
        verbose_name = "OfferStatus"
        verbose_name_plural = "OfferStatus"


class IPOStatus(models.Model):
    ipo_status = models.CharField(max_length=255, null=False)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(null=True, blank=True, editable=False)
    updated_by = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name="Updated By", blank=True, default=1)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.ipo_status}'

    class Meta:
        verbose_name = "IPOStatus"
        verbose_name_plural = "IPOStatus"


class ListingStatus(models.Model):
    listing_status = models.CharField(max_length=255, null=False)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(null=True, blank=True, editable=False)
    updated_by = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name="Updated By", blank=True, default=1)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.listing_status}'

    class Meta:
        verbose_name = "ListingStatus"
        verbose_name_plural = "ListingStatus"


class ListingType(models.Model):
    listing_type = models.CharField(max_length=255, null=False)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(null=True, blank=True, editable=False)
    updated_by = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name="Updated By", blank=True, default=1)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.listing_type}'

    class Meta:
        verbose_name = "ListingType"
        verbose_name_plural = "ListingType"
